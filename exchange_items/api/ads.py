from flask import Blueprint, request, jsonify
from crawler import Ad, Session
from sqlalchemy import select

ads = Blueprint("ads", __name__, url_prefix="/ads")

@ads.route('', methods=['GET'])
def get_ads():
    session = Session()
    try:
        # Get query parameters
        limit = request.args.get('limit', 10, type=int)
        offset = request.args.get('offset', 0, type=int)
        
        # Query with pagination
        query = select(Ad).limit(limit).offset(offset)
        ads = session.execute(query).scalars().all()
        
        return jsonify([{
            'id': ad.id,
            'ad_id': ad.ad_id,
            'list_id': ad.list_id,
            'subject': ad.subject,
            'price': ad.price,
            'category_name': ad.category_name,
            'area_name': ad.area_name,
            'region_name': ad.region_name,
            'body': ad.body,
            'longitude': ad.longitude,
            'latitude': ad.latitude,
            'location': ad.location
        } for ad in ads])
    finally:
        session.close()

@ads.route('<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    session = Session()
    try:
        ad = session.query(Ad).filter(Ad.ad_id == ad_id).first()
        if not ad:
            return jsonify({'error': 'Ad not found'}), 404
            
        return jsonify({
            'id': ad.id,
            'ad_id': ad.ad_id,
            'list_id': ad.list_id,
            'subject': ad.subject,
            'price': ad.price,
            'category_name': ad.category_name,
            'area_name': ad.area_name,
            'region_name': ad.region_name,
            'body': ad.body,
            'longitude': ad.longitude,
            'latitude': ad.latitude,
            'location': ad.location,
            'raw_data': ad.raw_data
        })
    finally:
        session.close()

@ads.route('', methods=['POST'])
def create_ad():
    session = Session()
    try:
        data = request.json
        ad = Ad(
            ad_id=data.get('ad_id'),
            list_id=data.get('list_id'),
            subject=data.get('subject'),
            price=data.get('price'),
            category_name=data.get('category_name'),
            area_name=data.get('area_name'),
            region_name=data.get('region_name'),
            body=data.get('body'),
            longitude=data.get('longitude'),
            latitude=data.get('latitude'),
            location=data.get('location'),
            raw_data=data.get('raw_data')
        )
        session.add(ad)
        session.commit()
        return jsonify({'message': 'Ad created successfully', 'id': ad.id}), 201
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()

@ads.route('<int:ad_id>', methods=['PUT'])
def update_ad(ad_id):
    session = Session()
    try:
        ad = session.query(Ad).filter(Ad.ad_id == ad_id).first()
        if not ad:
            return jsonify({'error': 'Ad not found'}), 404
            
        data = request.json
        for key, value in data.items():
            if hasattr(ad, key):
                setattr(ad, key, value)
                
        session.commit()
        return jsonify({'message': 'Ad updated successfully'})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()

@ads.route('<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    session = Session()
    try:
        ad = session.query(Ad).filter(Ad.ad_id == ad_id).first()
        if not ad:
            return jsonify({'error': 'Ad not found'}), 404
            
        session.delete(ad)
        session.commit()
        return jsonify({'message': 'Ad deleted successfully'})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        session.close() 

@ads.route('/first', methods=['GET'])
def get_first_ad():
    """Get first ad in collection
    Endpoint: /api/v1/ads/first
    Method: GET
    Request Params:
        - collection_id: ID of collection
    Response: First ad details with offers
    """
    session = Session()
    try:
        collection_id = request.args.get('collection_id')
        if not collection_id:
            return jsonify({
                'success': False,
                'error': 'collection_id is required'
            }), 400

        collection = session.query(Collection).filter(Collection.id == collection_id).first()
        if not collection or not collection.ads:
            return jsonify({
                'success': False,
                'error': 'Collection or ads not found'
            }), 404

        first_ad = collection.ads[0]
        return jsonify({
            'success': True,
            'data': {
                'id': str(first_ad.id),
                'name': first_ad.name,
                'short_description': first_ad.short_description,
                'description': first_ad.description,
                'image_url': first_ad.image_url,
                'seller_name': first_ad.seller_name,
                'location_distance': first_ad.location_distance,
                'total_offer': len(first_ad.offers),
                'offers': [{
                    'id': str(offer.id),
                    'ads_name': first_ad.name,
                    'owner_name': offer.owner.name,
                    'created_date': offer.created_date.isoformat(),
                    'status': offer.status
                } for offer in first_ad.offers]
            }
        })
    finally:
        session.close()

@ads.route('/next', methods=['GET'])
def get_next_ad():
    """Get next ad in collection
    Endpoint: /api/v1/ads/next
    Method: GET
    Request Params:
        - collection_id: ID of collection
        - current_index: Current ad index
    Response: Next ad details with offers
    """
    session = Session()
    try:
        collection_id = request.args.get('collection_id')
        current_index = int(request.args.get('current_index', 0))

        if not collection_id:
            return jsonify({
                'success': False,
                'error': 'collection_id is required'
            }), 400

        collection = session.query(Collection).filter(Collection.id == collection_id).first()
        if not collection or not collection.ads:
            return jsonify({
                'success': False,
                'error': 'Collection or ads not found'
            }), 404

        if current_index >= len(collection.ads) - 1:
            return jsonify({
                'success': False,
                'error': 'No more ads'
            }), 404

        next_ad = collection.ads[current_index + 1]
        return jsonify({
            'success': True,
            'data': {
                'id': str(next_ad.id),
                'name': next_ad.name,
                'short_description': next_ad.short_description,
                'description': next_ad.description,
                'image_url': next_ad.image_url,
                'seller_name': next_ad.seller_name,
                'location_distance': next_ad.location_distance,
                'total_offer': len(next_ad.offers),
                'offers': [{
                    'id': str(offer.id),
                    'ads_id': offer.ad_id,
                    'ads_name': next_ad.name,
                    'owner_id': offer.owner_id,
                    'owner_name': offer.owner.name,
                    'created_date': offer.created_date.isoformat(),
                    'status': offer.status
                } for offer in next_ad.offers]
            }
        })
    finally:
        session.close()
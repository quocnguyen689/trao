from flask import Blueprint, request, jsonify

from exchange_items.models import Collection
from crawler import Session
from sqlalchemy import select

# from exchange_items.utils import litellm_client

collections = Blueprint("collections", __name__, url_prefix="/collections")

@collections.route("", methods=["GET"])
def get_collections(user_id):
    """Get list of collections
    Endpoint: /api/collection
    Method: GET
    Response: Array of collections with total number of ads
    """
    session = Session()
    try:
        query = select(Collection)
        collections = session.execute(query).scalars().all()

        # hardcode info ads need to suggest
        ad_response = {
            "ad": {
                "subject": "Iphone 13 128Gb hồng, pin 100%",
                "body": "Máy đẹp keng, pin 100%, mua chưa đầy 1 năm, không trầy xước, fullbox.",
                "category_name": "Điện thoại",
                "region_name": "TP.HCM",
                "condition_ad_name": "Còn Mới 99%",
                "price_string": "1000000",
                "region": "TP.HCM"
            }
        }

        # collection_suggest = litellm_client.suggest_collections(ad_response)
        # print(collection_suggest)

        return jsonify({
            'success': True,
            'data': [{
                'id': str(c.id),
                'name': c.name,
                'icon_url': c.icon_url,
                'total_number_ads': 10
            } for c in collections]
        })
    finally:
        session.close()

@collections.route('/<int:collection_id>', methods=['GET'])
def get_collection(collection_id):
    """Get a single collection by ID"""
    session = Session()
    try:
        collection = session.query(Collection).filter(Collection.id == collection_id).first()
        if not collection:
            return jsonify({
                'success': False,
                'error': 'Collection not found'
            }), 404

        return jsonify({
            'success': True,
            'data': collection.to_dict()
        })
    finally:
        session.close()

@collections.route('/<int:collection_id>', methods=['GET'])
def get_collection_for_you(collection_id):
    """Get a single collection by ID"""
    session = Session()
    try:
        collection = session.query(Collection).filter(Collection.id == collection_id).first()
        if not collection:
            return jsonify({
                'success': False,
                'error': 'Collection not found'
            }), 404

        return jsonify({
            'success': True,
            'data': collection.to_dict()
        })
    finally:
        session.close()

@collections.route('/api/v1/collection', methods=['POST'])
def create_collection():
    """Create a new collection"""
    session = Session()
    try:
        data = request.json
        collection = Collection(
            name=data.get('name'),
            icon_url=data.get('icon_url')
        )
        session.add(collection)
        session.commit()

        return jsonify({
            'success': True,
            'data': collection.to_dict()
        }), 201
    except Exception as e:
        session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    finally:
        session.close()

@collections.route('/<int:collection_id>', methods=['PUT'])
def update_collection(collection_id):
    """Update a collection"""
    session = Session()
    try:
        collection = session.query(Collection).filter(Collection.id == collection_id).first()
        if not collection:
            return jsonify({
                'success': False,
                'error': 'Collection not found'
            }), 404

        data = request.json
        if 'name' in data:
            collection.name = data['name']
        if 'icon_url' in data:
            collection.icon_url = data['icon_url']

        session.commit()
        return jsonify({
            'success': True,
            'data': collection.to_dict()
        })
    except Exception as e:
        session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    finally:
        session.close()

@collections.route('/<int:collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    """Delete a collection"""
    session = Session()
    try:
        collection = session.query(Collection).filter(Collection.id == collection_id).first()
        if not collection:
            return jsonify({
                'success': False,
                'error': 'Collection not found'
            }), 404

        session.delete(collection)
        session.commit()
        return jsonify({
            'success': True,
            'data': {'message': 'Collection deleted successfully'}
        })
    except Exception as e:
        session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    finally:
        session.close()

@collections.route('/api/v1/ads/heart', methods=['POST'])
def heart_ad():
    """Save ad to favorites
    Endpoint: /api/v1/ads/heart
    Method: POST
    Request Body:
        - user_id: User ID
        - ad_id: Ad ID
    """
    session = Session()
    try:
        data = request.json
        user_id = data.get('user_id')
        ad_id = data.get('ad_id')

        if not user_id or not ad_id:
            return jsonify({
                'success': False,
                'error': 'user_id and ad_id are required'
            }), 400

        # Create user activity for favoriting ad
        # Implementation depends on UserActivity model

        return jsonify({
            'success': True,
            'data': {}
        })
    finally:
        session.close()

@collections.route('/api/v1/offer/status-update', methods=['PUT'])
def update_offer_status():
    """Update offer status
    Endpoint: /api/v1/offer/status-update
    Method: PUT
    Request Body:
        - ad_id: Ad ID
        - user_id: User ID
        - action_type: Action type
    """
    session = Session()
    try:
        data = request.json
        ad_id = data.get('ad_id')
        user_id = data.get('user_id')
        action_type = data.get('action_type')

        if not all([ad_id, user_id, action_type]):
            return jsonify({
                'success': False,
                'error': 'ad_id, user_id and action_type are required'
            }), 400

        # Update offer status
        # Implementation depends on Offer model

        return jsonify({
            'success': True,
            'data': {}
        })
    finally:
        session.close()
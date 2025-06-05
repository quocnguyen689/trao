import grpc
import ct_data_logic_multimodal_ad_listing.v1.interfaces_pb2 as interfaces
import ct_data_logic_multimodal_ad_listing.v1.methods_pb2_grpc as methods


def run():
    channel = grpc.insecure_channel('ct-data-logic-multimodal-ad-listing.default.svc.gke1.ct.dev:80')
    # channel = grpc.insecure_channel('localhost:50051')

    stub = methods.MultiModalListingServiceStub(channel)
    request = interfaces.ExtractListingInfoRequest(
        image_uris=[
            "gs://ct-sp-stag-ct-infra-gcs-ct-rapid-listing-processed/019677f8-05b4-765c-9a6a-1dfc5aa00f17.mp4_frames/frame_0001.jpg"],
        audio_uri="gs://ct-sp-stag-ct-infra-gcs-ct-rapid-listing-processed/019677f8-05b4-765c-9a6a-1dfc5aa00f17.wav",
        video_uri="")
    try:
        response = stub.ExtractListingInfo(request)
        print(response)
    except grpc.RpcError as e:
        print("Status code:", e.code())
        print("Details:", e.details())

        if e.trailing_metadata():
            for key, value in e.trailing_metadata():
                print(f"Metadata: {key} = {value}")
                if key == "error-code" and value == "cannot_recognize":
                    print("⚠️ Custom error: Cannot recognize input")
    # print("Response:", response)


if __name__ == '__main__':
    run()

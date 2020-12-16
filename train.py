import json
from tensorflow.keras.optimizers import Adam, SGD
from models.ssd import SSD300_VGG16_ORIGINAL
from losses import SSD_LOSS
from data_generators.voc import SSD_VOC_DATA_GENERATOR
from base_networks import VGG16_D

if __name__ == "__main__":
    # base_model = VGG16_D(num_classes=20)
    with open("configs/ssd300_vgg16_original.json") as config_file:
        config = json.load(config_file)

    model = SSD300_VGG16_ORIGINAL(config)
    # model.compile(
    #     optimizer=SGD(lr=0.001, momentum=0.9, decay=0.0005, nesterov=False),
    #     loss=SSD_LOSS(
    #         alpha=config["training"]["alpha"],
    #         min_negative_boxes=config["training"]["min_negative_boxes"],
    #         negative_boxes_ratio=config["training"]["negative_boxes_ratio"]
    #     ).compute
    # )
    # # data_generator = SSD_VOC_DATA_GENERATOR(
    # #     samples=["data/test.jpg data/test.xml"],
    # #     config=config
    # # )

    # model.fit(
    #     x=SSD_VOC_DATA_GENERATOR(
    #         samples=["data/test.jpg data/test.xml"],
    #         config=config
    #     ),
    #     batch_size=1,
    #     epochs=1,
    #     steps_per_epoch=1,
    # )

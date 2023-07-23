from fastapi import FastAPI, File, UploadFile
import uvicorn


# MODEL = tf.keras.models.load_model("potatoes.h5")
#
# CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]


app = FastAPI()
@app.get("/ping")
async def ping():
    return "Finally, I made it run"


@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    # image = read_file_as_image(await file.read())
    # img_batch = np.expand_dims(image, 0)
    #
    # predictions = MODEL.predict(img_batch)
    #
    # predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    # confidence = np.max(predictions[0])
    # return {
    #     'class': predicted_class,
    #     'confidence': float(confidence)
    # }
    pass



if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "3e62a8c1-7a92-4f6d-ae38-9ba2c6a18f01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "main.py created!\n"
     ]
    }
   ],
   "source": [
    "main_code = \"\"\"from fastapi import FastAPI\n",
    "from pydantic import BaseModel\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "model = joblib.load(\"flushing_model.pkl\")\n",
    "app = FastAPI()\n",
    "\n",
    "class HouseFeatures(BaseModel):\n",
    "    gross_square_feet: float\n",
    "    land_square_feet: float\n",
    "    year_built: float\n",
    "    residential_units: float\n",
    "\n",
    "@app.get(\"/\")\n",
    "def home():\n",
    "    return {\"message\": \"Flushing Queens House Price Predictor\"}\n",
    "\n",
    "@app.post(\"/predict\")\n",
    "def predict(features: HouseFeatures):\n",
    "    X = np.array([[\n",
    "        features.gross_square_feet,\n",
    "        features.land_square_feet,\n",
    "        features.year_built,\n",
    "        features.residential_units\n",
    "    ]])\n",
    "    prediction = model.predict(X)\n",
    "    return {\n",
    "        \"estimated_price\": f\"${prediction[0]:,.0f}\",\n",
    "        \"neighborhood\": \"Flushing, Queens NYC\"\n",
    "    }\n",
    "\"\"\"\n",
    "\n",
    "with open(\"main.py\", \"w\") as f:\n",
    "    f.write(main_code)\n",
    "\n",
    "print(\"main.py created!\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

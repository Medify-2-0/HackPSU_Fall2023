# HackPSU2023
<h1>Brain Tumor Detection Model</h1>

<h2>Introduction</h2>
During our Hackathon initiative, our team embarked on a pivotal mission to tackle a pressing medical concern: the detection of brain tumors. Harnessing the power of deep learning, we developed a model capable of identifying brain tumors with an astounding 94% accuracy. This innovation holds the promise of significantly curtailing human diagnostic errors. In regions where medical expertise is scarce, our model can swiftly provide an assessment of the likelihood of a brain tumor. This rapid preliminary diagnosis ensures that individuals receive prompt attention, eliminating prolonged waiting times for specialist consultations which could be life-threatening. Essentially, our model serves as a lifesaver, ensuring early diagnosis and intervention, pivotal elements in enhancing patient survival rates.

In a vast and diverse nation like India, where access to advanced medical training might be limited in certain areas, our model carries additional significance. Our integrated 3D visualization tool serves as an educational asset, enabling students and budding medical professionals to gain a tangible understanding of the appearance of brain tumors. By juxtaposing their predictions against the model's determinations, they can refine their diagnostic skills, bridging the gap between theoretical knowledge and practical application. This not only fosters a deeper comprehension but also equips the next generation with hands-on expertise crucial for early and accurate tumor detection.

<h2>Technology Stack</h2>

<h3>Convolutional Neural Networks (CNN)</h3>: We leveraged the power of CNNs, which are a category of neural networks especially potent for tasks such as image recognition and classification. Given the visual nature of brain scans, CNNs were the natural choice for our project.

<h3>TensorFlow & Keras</h3>: Our model was implemented using TensorFlow, an end-to-end open-source platform for machine learning, in combination with Keras, a high-level neural networks API. These tools facilitated efficient model training, testing, and validation.

<h3>VTK & Matplotlib</h3>: For a comprehensive understanding of the brain scans and the presence of tumors, we integrated 3D plotting capabilities into our solution. We used VTK (The Visualization Toolkit) along with matplotlib.pyplot to create insightful visualizations, allowing medical professionals to better comprehend the nature and location of detected tumors.

<h3>Flask</h3>: Serving as our Python framework, Flask seamlessly used in conjunction with HTML and CSS, presenting our project in an interactive and user-friendly manner. Its flexibility and simplicity ensured smooth deployment and integration of our brain tumor detection model with the web interface.

<h2>Dataset</h2>
Our team utilized a dataset sourced from Kaggle, a reputable platform known for hosting diverse datasets for machine learning and data analysis projects. The dataset contained labeled brain scans, which proved invaluable for training our model and validating its performance. You can access the dataset <a href=”https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection”>here</a>

Conclusion
Harnessing the power of deep learning and the capabilities of visualization tools, our project stands as a testament to how technology can contribute significantly to the medical field. With an accuracy rate of 94%, our brain tumor detection model has the potential to aid medical professionals in diagnosing conditions early and accurately.

Datasets:
1) https://www.kaggle.com/datasets/yasserhessein/dataset-alzheimer/data
2) https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection
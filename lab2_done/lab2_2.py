def noisy():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image

    try:
        ideal_image = cv2.imread("images/source/mustang_2.jpg")[0:, 0:, 2]
    except FileNotFoundError:
        print("File is not found")
    # mu - Среднее значание случ. величины, sigma - ср. квадратич. отклонение
    mu, sigma = 0.20, 0.03
    gauss_Noise = np.random.normal(mu, sigma, size=ideal_image.shape)
    noised_Image = ideal_image + gauss_Noise
    noised_Image2 = np.random.poisson(ideal_image)
    # noised_Image2[noised_Image2 > 255] = 255
    cv2.imshow("noised_Image", noised_Image)  # Showing image with gauss noise (Изображение с гаусовским шумом)
    cv2.imwrite("images/noise/noised_Image.jpg", noised_Image)
    cv2.imshow("ideal_image", ideal_image)  # Showing original image
    cv2.imwrite("images/noise/ideal_image.jpg", ideal_image)
    cv2.imshow("gauss_Noise", gauss_Noise)  # Showing gauss noise
    cv2.imwrite("images/noise/gauss_Noise.jpg", gauss_Noise)
    img = Image.fromarray(noised_Image2, 'RGB')
    img.show()  # Showing image with poisson (Изображение с пуассоновским шумом)
    img.save("images/noise/poisson_Noise.jpg")
    count2, bins2, ignored2 = plt.hist(noised_Image, 5, density=True)
    plt.title("gauss noise")
    plt.show()
    count, bins, ignored = plt.hist(noised_Image2, 5, density=True)
    plt.title("poisson noise")
    plt.show()
    cv2.waitKey(0)
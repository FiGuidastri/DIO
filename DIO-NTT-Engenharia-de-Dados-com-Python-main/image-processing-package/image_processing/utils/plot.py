import matplotlib.pyplot as plt

def plot_img(img):
    plt.figure(figsize=(12,4))
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()
    
def plot_result(*args):
    number_imgs = len(args)
    fig, axis = plt.subplots(nrow=1, ncols = number_imgs, figsize=(12,4))
    names_list = ['Imagem {}'.format(i) for i in range(1, number_imgs)]
    names_list.append('Resultado')
    for ax, name, image in zip(axis, names_list, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()
    
def plot_histogram(img):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharex=True, sharey=True)
    color_list = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_list)):
        ax.set_title('{} histograma'.format(color.title()))
        ax.hist(img[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt.show()
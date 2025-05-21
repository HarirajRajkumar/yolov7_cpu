with open('train.txt', "a+") as f:
    img_list = os.listdir(train_img_path)
    for img in img_list:
        f.write(os.path.join(train_img_path,img+"\n"))
    print("Done")

with open('val.txt', "a+") as f:
    img_list = os.listdir(val_img_path)
    for img in img_list:
        f.write(os.path.join(val_img_path,img+"\n"))
    print("Done")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='yolo7.pt', help='initial weights path')
    parser.add_argument('--cfg', type=str, default='', help='model.yaml path')
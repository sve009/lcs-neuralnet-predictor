from lcs_wr_nn import *
import numpy as np

model = None

while True:
    s = input(">>> ")
    (s, _, args) = s.partition(' ')

    print(args)

    if s == "q":
        break
    elif s == "help" or s == "?":
        print("Available commands are 'create', 'train', 'evaluate', 'save', 'load', or 'predict x' where x is a 24 dimensional vector of float32s'")
    elif s == "create":
        model = create_model()
        print("Model created")
    elif s == "train":
        if model == None:
            print("There is no current model")
        else: 
            train_model(model, 500)
            print("Model evaluated")
    elif s == "evaluate":
        if model == None:
            print("There is no current model")
        else:
            evaluate_model(model)
    elif s == "save":
        if model == None:
            print("There is no current model")
        else:
            args = args.strip()
            save_model(model, args)
            print("Model saved")
    elif s == "load":
        if model == None:
            model = create_model()
            load_weights(model, args)
        else:
            load_weights(model, args)
        print("Weights loaded")
    elif s == "predict":
        if model == None:
            print("There is no current model")
        else:
            vec = args.strip().split(' ')
            arr = []
            for word in vec:
                num = float(word)
                arr.append(num)
            x = np.array(arr)
            print("The predicted WR is: " + str(model_predict(model, x)), flush=True)




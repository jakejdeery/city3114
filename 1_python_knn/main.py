# city3114_proc1, jake deery, 2020

# 'include' i'm a cpp developer and its late okay, let me write this like a goddamn conapp
from sklearn import datasets
from sklearn import neighbors
from sklearn import linear_model



# i know python supports globally scoped code but thats utterly rancid even traditional c doesnt do that
class main():
    def __init__(self): # why is this syntax a thing
        #
        # vars
        # global scoping is gross so this crap goes here
        digitsData, digitsGroundTruth = datasets.load_digits(return_X_y=True)  # load the sklearn digits dataset for
        # some juicy preloaded goodness ayyyy thank based jesus for sklearn, also that bool splits the dataset into
        # data & target

        knn = neighbors.KNeighborsClassifier() # this is the classifier which should do some magic for us which i will
        # of course fully explain and know exactly what i mean, totally, in my report

        logistic = linear_model.LogisticRegression(max_iter=1000) # a form of linear regression. this will simply act
        # as a comparison against the knn -- to see if the values are close which they are because i am a god

        #
        # init stuff
        # say aite, innit (get it?)
        print("[I] CITY3114_PROC1, Jake Deery, 2020") # what chimpanzee decided not requiring a ; was a good idea
        print("") # what chimpanzee decided not requiring a \n was a good idea

        #
        # do some prep
        # ... prior to the actual learning algorithm
        digitsData = digitsData / digitsData.max()  # divide the list's contents by the largest value within
        nSamples = len(digitsData) # fetches the total length of the 'array' i know its a list okaaaaaaaay!

        trainData = digitsData[:int(.9 * nSamples)]  # take the first 90% of the data as our set
        trainGroundTruth = digitsGroundTruth[:int(.9 * nSamples)] # "  "
        testData = digitsData[int(.9 * nSamples):] # take the last 10% of the data as our set
        testGroundTruth = digitsGroundTruth[int(.9 * nSamples):] # "  "

        #
        # print the final results
        # i will discuss more on what is happening here within my report
        print('[I] KNN score: %f'
              % knn.fit(trainData, trainGroundTruth).score(testData, testGroundTruth)) # do the knn magic
        print('[I] Logistic Regression score: %f'
              % logistic.fit(trainData, trainGroundTruth).score(testData, testGroundTruth)) # do the logistic magic

    def __del__(self):
        # taaaaraaaaaaaa!
        print("")
        print("Bye!")


#
#
# run class & delet
doProc = main()
del doProc

#
# python sucks
# bye

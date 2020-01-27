def main():

    def func(question, true, false):
        choice = input(question)
        if choice == "y":
            true()
        else:
            false()

    def pneumonia():
        print("Possibilities include preumonia or infection of airways")

    def infection():
        print("Possibilities include viral infection")

    def insufficient():
        print("Insufficcient information to list possibilities")

    def throat_infection():
        print("Possibilities includes a throat infection")

    def kidney_infection():
        print("Possibilities includes kidney infection")

    def urinary_infection():
        print("Possibilities includes a urinary tract infection")

    def suntroke():
        print("Possibilities sunstroke or heat exhausion")

    def sun():
        func("Have you spent the day in the sun or in hot conditions? y/n: \n", suntroke, insufficient)

    def urinating():
        func("Do you have pain urinating or are urinating more often y/n: \n", urinary_infection, sun)

    def back_pain():
        func("Do you have back pain just above the waist with chills and fever? y/n: \n", kidney_infection, urinating)

    def sore_throat():
        func("Do you have a sore throat? y/n: \n", throat_infection, back_pain)

    def rash():
        func("Do you have a rash? y/n:\n", insufficient, sore_throat)

    def aching():
        func("Do you have aching bones or aching joints? y/n:\n", infection, rash)

    def headache():
        func("Do you have a headache? y/n: \n", infection, aching)

    def short_of_breath():
        func("Are you short of breath or wheezing or coughing up phlegm? y/n: \n", pneumonia, headache)

    def menigitis():
        print("Possibilities include menigitis")

    def digestive():
        print("Possibilities include digestive tract infection")

    def diarrhea():
        func("Are you vomiting or had diarrhea? y/n: \n", digestive, aching)

    def any_of_following():
        func("Are you experiencing any of the following: pain when bending your head forward, nausea or vomitting, bright light hurting your eyes, drowsiness or confusion? y/n: \n", menigitis, diarrhea)

    def headache_no_cough():
        func("Do you have a headache? y/n: \n", any_of_following, aching)

    func("Are you coughing? y/n:\n", short_of_breath, headache_no_cough)


main()

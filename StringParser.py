__author__ = 'sambhav'


def parseOfString(passedval):

    more2="morethan2pax";

    if "more than two person" in passedval:
        passedval=passedval.replace("more than two person",more2);

    if "more than 2 person" in passedval:
        passedval=passedval.replace("more than 2 person",more2);

    if "morethan2paxs" in passedval:
        passedval=passedval.replace("morethan2paxs",more2);

    if "under 100" in passedval:
        passedval=passedval.replace("under 100","under100");


    return passedval


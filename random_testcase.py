import random
group = [
	"00Uncorrelated",
	"01WeaklyCorrelated",
	"02StronglyCorrelated",
	"03InverseStronglyCorrelated",
	"04AlmostStronglyCorrelated",
	"05SubsetSum",
	"06UncorrelatedWithSimilarWeights",
	"07SpannerUncorrelated",
	"08SpannerWeaklyCorrelated",
	"09SpannerStronglyCorrelated",
	"10MultipleStronglyCorrelated",
	"11ProfitCeiling",
	"12Circle"
]
size_group = [
	"n00050",
	"n00100",
	"n00200",
	"n00500",
	"n01000",
	"n02000",
	"n05000",
	"n10000"
]   
   
for i in group:
    for j in size_group:
        name = i + '/' + j
        rand = random.randint(1, 10)

        if rand in (2, 5):
            print("\"original_data/" + name + "/R01000/s0" + str(random.randint(10, 99)), end = '",\n') 
        elif rand == 1:
            print("\"original_data/" + name + "/R01000/s00" + str(random.randint(0, 9)), end = '",\n')
        elif rand == 10:
            print("\"original_data/" + name + "/R10000/s00" + str(random.randint(0, 9)), end = '",\n')
        else:
            print("\"original_data/" + name + "/R10000/s0" + str(random.randint(10, 99)), end = '",\n')

        
# copy this output to 'input array' in file get_testcase.py
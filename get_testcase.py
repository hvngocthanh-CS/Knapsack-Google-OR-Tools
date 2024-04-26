def input_data():
	input =  [
		"original_data/00Uncorrelated/n00050/R10000/s002",
		"original_data/00Uncorrelated/n00100/R01000/s036",
		"original_data/00Uncorrelated/n00200/R10000/s010",
		"original_data/00Uncorrelated/n00500/R10000/s057",
		"original_data/00Uncorrelated/n01000/R10000/s024",
		"original_data/00Uncorrelated/n02000/R01000/s015",
		"original_data/00Uncorrelated/n05000/R10000/s019",
		"original_data/00Uncorrelated/n10000/R10000/s032",
  
		"original_data/01WeaklyCorrelated/n00050/R01000/s049",
		"original_data/01WeaklyCorrelated/n00100/R01000/s008",
		"original_data/01WeaklyCorrelated/n00200/R01000/s006",
		"original_data/01WeaklyCorrelated/n00500/R01000/s009",
		"original_data/01WeaklyCorrelated/n01000/R10000/s065",
		"original_data/01WeaklyCorrelated/n02000/R01000/s007",
		"original_data/01WeaklyCorrelated/n05000/R10000/s082",
		"original_data/01WeaklyCorrelated/n10000/R10000/s025",
  
		"original_data/02StronglyCorrelated/n00050/R10000/s006",
		"original_data/02StronglyCorrelated/n00100/R01000/s020",
		"original_data/02StronglyCorrelated/n00200/R10000/s037",
		"original_data/02StronglyCorrelated/n00500/R01000/s026",
		"original_data/02StronglyCorrelated/n01000/R10000/s028",
		"original_data/02StronglyCorrelated/n02000/R10000/s030",
		"original_data/02StronglyCorrelated/n05000/R01000/s006",
		"original_data/02StronglyCorrelated/n10000/R01000/s064",
  
		"original_data/03InverseStronglyCorrelated/n00050/R10000/s004",
		"original_data/03InverseStronglyCorrelated/n00100/R10000/s092",
		"original_data/03InverseStronglyCorrelated/n00200/R01000/s001",
		"original_data/03InverseStronglyCorrelated/n00500/R10000/s046",
		"original_data/03InverseStronglyCorrelated/n01000/R10000/s003",
		"original_data/03InverseStronglyCorrelated/n02000/R10000/s015",
		"original_data/03InverseStronglyCorrelated/n05000/R10000/s005",
		"original_data/03InverseStronglyCorrelated/n10000/R10000/s056",
  
		"original_data/04AlmostStronglyCorrelated/n00050/R10000/s018",
		"original_data/04AlmostStronglyCorrelated/n00100/R01000/s068",
		"original_data/04AlmostStronglyCorrelated/n00200/R01000/s098",
		"original_data/04AlmostStronglyCorrelated/n00500/R10000/s065",
		"original_data/04AlmostStronglyCorrelated/n01000/R10000/s017",
		"original_data/04AlmostStronglyCorrelated/n02000/R10000/s012",
		"original_data/04AlmostStronglyCorrelated/n05000/R10000/s031",
		"original_data/04AlmostStronglyCorrelated/n10000/R10000/s013",
  
		"original_data/05SubsetSum/n00050/R10000/s035",
		"original_data/05SubsetSum/n00100/R10000/s013",
		"original_data/05SubsetSum/n00200/R01000/s077",
		"original_data/05SubsetSum/n00500/R10000/s082",
		"original_data/05SubsetSum/n01000/R10000/s094",
		"original_data/05SubsetSum/n02000/R10000/s044",
		"original_data/05SubsetSum/n05000/R01000/s005",
		"original_data/05SubsetSum/n10000/R10000/s031",
  
		"original_data/06UncorrelatedWithSimilarWeights/n00050/R10000/s019",
		"original_data/06UncorrelatedWithSimilarWeights/n00100/R10000/s040",
		"original_data/06UncorrelatedWithSimilarWeights/n00200/R10000/s008",
		"original_data/06UncorrelatedWithSimilarWeights/n00500/R10000/s006",
		"original_data/06UncorrelatedWithSimilarWeights/n01000/R01000/s010",
		"original_data/06UncorrelatedWithSimilarWeights/n02000/R01000/s002",
		"original_data/06UncorrelatedWithSimilarWeights/n05000/R01000/s068",
		"original_data/06UncorrelatedWithSimilarWeights/n10000/R01000/s091",
  
		"original_data/07SpannerUncorrelated/n00050/R01000/s022",
		"original_data/07SpannerUncorrelated/n00100/R10000/s064",
		"original_data/07SpannerUncorrelated/n00200/R10000/s034",
		"original_data/07SpannerUncorrelated/n00500/R10000/s014",
		"original_data/07SpannerUncorrelated/n01000/R01000/s009",
		"original_data/07SpannerUncorrelated/n02000/R10000/s080",
		"original_data/07SpannerUncorrelated/n05000/R10000/s079",
		"original_data/07SpannerUncorrelated/n10000/R10000/s050",
  
		"original_data/08SpannerWeaklyCorrelated/n00050/R01000/s005",
		"original_data/08SpannerWeaklyCorrelated/n00100/R10000/s083",
		"original_data/08SpannerWeaklyCorrelated/n00200/R10000/s079",
		"original_data/08SpannerWeaklyCorrelated/n00500/R10000/s055",
		"original_data/08SpannerWeaklyCorrelated/n01000/R10000/s094",
		"original_data/08SpannerWeaklyCorrelated/n02000/R01000/s005",
		"original_data/08SpannerWeaklyCorrelated/n05000/R01000/s085",
		"original_data/08SpannerWeaklyCorrelated/n10000/R01000/s006",
  
		"original_data/09SpannerStronglyCorrelated/n00050/R01000/s019",
		"original_data/09SpannerStronglyCorrelated/n00100/R10000/s053",
		"original_data/09SpannerStronglyCorrelated/n00200/R01000/s024",
		"original_data/09SpannerStronglyCorrelated/n00500/R10000/s035",
		"original_data/09SpannerStronglyCorrelated/n01000/R10000/s029",
		"original_data/09SpannerStronglyCorrelated/n02000/R01000/s098",
		"original_data/09SpannerStronglyCorrelated/n05000/R10000/s083",
		"original_data/09SpannerStronglyCorrelated/n10000/R10000/s046",
  
		"original_data/10MultipleStronglyCorrelated/n00050/R10000/s072",
		"original_data/10MultipleStronglyCorrelated/n00100/R10000/s029",
		"original_data/10MultipleStronglyCorrelated/n00200/R10000/s093",
		"original_data/10MultipleStronglyCorrelated/n00500/R01000/s081",
		"original_data/10MultipleStronglyCorrelated/n01000/R10000/s037",
		"original_data/10MultipleStronglyCorrelated/n02000/R01000/s007",
		"original_data/10MultipleStronglyCorrelated/n05000/R01000/s013",
		"original_data/10MultipleStronglyCorrelated/n10000/R10000/s092",
  
		"original_data/11ProfitCeiling/n00050/R10000/s017",
		"original_data/11ProfitCeiling/n00100/R01000/s033",
		"original_data/11ProfitCeiling/n00200/R10000/s026",
		"original_data/11ProfitCeiling/n00500/R10000/s029",
		"original_data/11ProfitCeiling/n01000/R01000/s010",
		"original_data/11ProfitCeiling/n02000/R10000/s008",
		"original_data/11ProfitCeiling/n05000/R10000/s023",
		"original_data/11ProfitCeiling/n10000/R10000/s042",
  
		"original_data/12Circle/n00050/R10000/s056",
		"original_data/12Circle/n00100/R10000/s048",
		"original_data/12Circle/n00200/R01000/s010",
		"original_data/12Circle/n00500/R01000/s076",
		"original_data/12Circle/n01000/R10000/s035",
		"original_data/12Circle/n02000/R01000/s022",
		"original_data/12Circle/n05000/R10000/s045",
		"original_data/12Circle/n10000/R10000/s077",
	]
	return input
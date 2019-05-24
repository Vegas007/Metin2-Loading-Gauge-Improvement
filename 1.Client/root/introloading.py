# Search for:
			self.loadingGage.SetPercentage(2+98*p/100, 100)
			
# Add after:
			self.loadingGage.SetPercentage(p, 160)
		
# Search for:
		self.__SetProgress(0)
		
# Add after:
		tmpLoadStepList = tuple(zip(*self.loadStepList))[0]
		for progress in range(tmpLoadStepList[0], tmpLoadStepList[-1] + 1):
			if progress not in tmpLoadStepList:
				self.loadStepList.append((progress, lambda: None))
			
		self.loadStepList.sort()

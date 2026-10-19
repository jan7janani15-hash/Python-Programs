from abc import ABC,abstractmethod
import statistics
class BaseDataTransformer(ABC):
    def transform(self,data):
        pass
class NormalizerTransformer(BaseDataTransformer):
    def transform(self,data):
        maximum=max(data)
        return [round(x / maximum, 2) for x in data]
class StandardizerTransformer(BaseDataTransformer):
    def transform(self,data):
        mean=statistics.mean(data)
        std=statistics.pstdev(data)
        return[round((x-mean)/std,2) for x in data]
norm=NormalizerTransformer()
std_t=StandardizerTransformer()
print("Normalized :",norm.transform([10,20,50,100]))
print("Standardized:",std_t.transform([10,20,30,40,50]))
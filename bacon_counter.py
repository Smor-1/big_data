from mrjob.job import MRJob

#function with yield returns a generator:
#generators are like a list, but not stored 
#in memory which is good for large files
class Bacon_count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1
    def reducer(self, key, values):
        yield key, sum(values)
        
if __name__ == "__main__":
   Bacon_count.run()


#to run in the terminal say: python bacon_counter.py input.txt
#make sure its PythonData environment 

import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    probdist = {}
    if bool(corpus.get(page)):
        for link in corpus.keys():
            probdist.update({link : (1-damping_factor)/len(corpus.keys())})
        for link in corpus[page]:
            probdist.update({link : probdist.get(link)+damping_factor/len(corpus[page])})
        return probdist
    else:
        for link in corpus.keys():
            probdist.update({link : 1/len(corpus.keys())})
        return probdist
    
    
    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    Random = random.random()
    current_page = None
    Sum = 0
    for key in corpus.keys():
        pagerank.update({key : 0})
    
    for key in corpus.keys():
        Sum += 1/len(corpus)
        if Sum > Random:
            pagerank.update({key : pagerank.get(key) + 1})
            current_page = key
            break
    
    for i in range(n-1):
        Probdist = transition_model(corpus, current_page, damping_factor)
        Random = random.random()
        Sum = 0
        for key in Probdist.keys():
            Sum += Probdist.get(key)
            if Sum > Random:
                pagerank.update({key : pagerank.get(key) + 1})
                current_page = key
                break
    for key in pagerank.keys():
        pagerank.update({key : pagerank.get(key)/n})
    return pagerank
    
        
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    Dict = {}
    difference = 1
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    for key in corpus:
        Dict.update({key : 1/len(corpus)})
    
    while difference > .001:
        for key in Dict:
            before = Dict.get(key)
            Sum = 0
            for key2 in Dict:
                if key in corpus.get(key2):
                    Sum += Dict.get(key2)/len(corpus.get(key2))
                if len(corpus.get(key2)) == 0:
                    Sum += Dict.get(key2)/len(corpus)
            Dict.update({key : (1-damping_factor)/len(corpus) + damping_factor*Sum})
            if not isinstance(difference, int) or difference > abs(before-Dict.get(key)):
                difference = abs(before-Dict.get(key))
    return Dict
            
    raise NotImplementedError    
                    

if __name__ == "__main__":
    main()

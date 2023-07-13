'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
import re
class Solution:
    def dfs(self, frm, htmlParser, visited):
        domain = lambda x: re.search('https?://([A-Za-z_0-9.-]+).*', x).group(1)
        """Recusrsive DFS traversal of Graph."""
        visited.add(frm)
        yield frm
        for url in htmlParser.getUrls(frm):
            if domain(url) == self.startUrlDomain and url not in visited:
                yield from self.dfs(url, htmlParser, visited)
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = lambda x: re.search('https?://([A-Za-z_0-9.-]+).*', x).group(1)
        self.startUrlDomain = domain(startUrl)
        return [url for url in self.dfs(startUrl, htmlParser, set())]

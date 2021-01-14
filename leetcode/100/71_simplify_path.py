class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == "":
            return ""
        files = ['']
        index = 0

        paths = path.split('/')

        for filestr in paths:
            if filestr == '.' or filestr == '' or filestr == '/':
                continue
            elif filestr == '..':
                if index > 0:
                    index -= 1
            else:
                index += 1
                if len(files) <= index:
                    files.append(filestr)
                else:
                    files[index] = filestr


        # print(files, index)
        if index == 0:
            return '/'
        else:
            return '/'.join(files[:index+1])

s = Solution()
print(s.simplifyPath("/home//foo/")=='/home/foo')
print(s.simplifyPath("/a/./b/../../c/")=='/c')
print(s.simplifyPath("") == '')
print(s.simplifyPath("/a/../../b/../c//.//") == '/c')
print(s.simplifyPath("/a//b////c/d//././/..") == '/a/b/c')
print(s.simplifyPath("/../../../../") == '/')
print(s.simplifyPath("/a/b/c/d//../../../../") == '/')
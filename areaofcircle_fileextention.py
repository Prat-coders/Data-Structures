# area of a circle
ask_from_user = float(input('Input the radius of the circle: '))
pie_value = 3.141592653589793238

area_of_circle = pie_value * ask_from_user**2
print(f'The area of the circle with radius {ask_from_user} is: {area_of_circle}')

# file extention

ask_user= input('Input the Filename: ')
extension= ask_user.split('.')
print(extension)
if extension[1]== 'py':
    print("The extension of the file is : 'python'")
else :
    print('The file is of other extension.')

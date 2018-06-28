# Web application for running the Compton Building & Remodling Site
from flask import Flask, render_template, json, send_file, url_for
from random import randint

app = Flask(__name__)

VERBOSE = True

def printPictures(pictureDict):
    print('Compton Building and Remodeling Pictures')
    for remodelType, typeNames in pictureDict.items():
        print('\t' + remodelType)
        for project, projectPictures in typeNames.items():
            print('\t\t' + project)
            for picture in projectPictures:
                print('\t\t\t' + picture)


bathroomNames = ['Bathroom A']
kitchenNames = ['Kitchen A', 'Kitchen B', 'Kitchen C']
remodelTypes = ['Bathrooms', 'Kitchens']
remodelPictures = dict()

bathroomPictures = dict()
kitchenPictures = dict()
remodelNames = dict()

bathroomPictures['Bathroom A'] = []
bathroomPictures['Bathroom A'].append('bathroom2.jpeg')

kitchenPictures['Kitchen A'] = []
kitchenPictures['Kitchen A'].append('kitchenA1.jpg')
kitchenPictures['Kitchen A'].append('kitchenA2.jpg')
kitchenPictures['Kitchen B'] = []
kitchenPictures['Kitchen B'].append('kitchen2.jpeg')
kitchenPictures['Kitchen C'] = [];
kitchenPictures['Kitchen C'].append('kitchen_example.jpeg')


remodelPictures['Bathrooms'] = bathroomPictures
remodelPictures['Kitchens'] = kitchenPictures
remodelNames['Bathrooms'] = bathroomNames
remodelNames['Kitchens'] = kitchenNames
# for i in range(0, len(remodelTypes)):
#     remodelName = remodelTypes[i]
#     # Check if the list already exits
#     if remodelName not in remodelPictures:
#         # If it doesn't make a new list
#         remodelPictures[remodelName] = []
if VERBOSE:
    printPictures(remodelPictures)



@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/ComptonBuilding')
# def compton_building_homepage():
#     return render_template('index.html')

@app.route('/kitchens')
def kitchens():
    return render_template('kitchens.html')

@app.route('/bathrooms')
def bathrooms():
    return render_template('bathrooms.html')

@app.route('/kitchenA.html')
def kitchenA():
    return render_template('kitchenA.html')

@app.route('/getImage/<string:imageName>')
def getImage(imageName):
    print('Returning image: ', imageName)
    return send_file('static/images/' + imageName, mimetype='image/jpeg')

@app.route('/imageURL')
def getImageURL():
    return url_for('static/images')

@app.route('/ComptonBuilding')
def homeTest():
    pagePictures = []
    # Get a random name for each type
    for remodelType, typePictures in remodelPictures.items():
        # Number of pictures in each type
        # Get the first set of pictures
        pictures = next (iter (typePictures.values()))
        print(pictures)
        length = len(pictures)
        print('Length: ' + str(length))
        index = randint(0, length-1)
        print('The pictures')
        print(typePictures)
        pagePictures.append(pictures[index])
         
    # return render_template('javascript_home.html')     
    return render_template('javascript_home.html', remodelTypes=remodelTypes, pagePictures=pagePictures)

@app.route('/remodelType/<string:remodelType>')
def rooms(remodelType):
    print('The room requested is: ', remodelType)
    remodelNames_ = remodelNames[remodelType]
    
    # Get the cover image
    pagePictures = []
    # Get a random name for each type
    i = 0
    for remodelName, remodelPicture in remodelPictures[remodelType].items():
        # Number of pictures in each type
        # Get the first set of pictures
        print(str(i));
        print('remodelName: ' + remodelName)
        print(remodelPicture)
        length = len(remodelPicture)
        print('Length: ' + str(length))
        index = randint(0, length-1)
        pagePictures.append(remodelPicture[index])
    
    return render_template('remodelType.html', remodelType=remodelType, remodelNames=remodelNames_, imageNames = pagePictures)

@app.route('/remodelType/<string:remodelType>/<string:remodelName>')
def remodel(remodelType, remodelName):
    print('Remodel Type: ' + remodelType + '\n\tRemodel Name: ' + remodelName)
    
    remodelImages = remodelPictures[remodelType][remodelName]
    return render_template('remodel.html', remodelImages=remodelImages, remodelName=remodelName)    

@app.route('/bathroom_test')
def test():
    return render_template('javascript_example.html', bathroom_names=kitchenNames)

if __name__ == "__main__":
    # Have the server restart on code change
    print(app.instance_path)
    app.run(debug=True)
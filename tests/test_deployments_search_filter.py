#FIXTURE:
    #create a deployment with mimimum data:
    #New Deployment
    #select RHV or OSP
    #set Deployment Name and Passwords
    #set Update Availability
    #set Red Hat Insights
    #click Next, click Cancel, click Exit&Save
#Run this fixture twice or three times to generate deployments

#TEST:
    #login
    #go to deployments page
    #get names of all the deployments
    #test cases:
        #input one of the names into search box
            #check that only matching deployment is displayed
        #delete everything from the search box
            #check that all of the deployments are displayed
        #input random string into search box
            #check that none of the deployments are displayed if there isn't a match

#FINALIZER
    #go to deployments page
    #delete all deployments

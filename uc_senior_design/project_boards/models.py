# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
    

'''
Object that stores information about the degree program for 
a set of senior design projects. 
'''
@python_2_unicode_compatible 
class DegreeProgram(models.Model):
    
    def __str__(self):
        return unicode(self.degree_program_name)
    
    degree_program_name = models.TextField(unique=True)

'''
Model describing a single senior design project. This data is displayed 
as an individual project with data.
'''
@python_2_unicode_compatible 
class Project(models.Model):
    
    def __str__(self):
        return unicode(self.log_form())
        
    def log_form(self):
        niceOutputString = ''
        niceOutputString += self.board_image_url + '\n'
        niceOutputString += self.abstract + '\n'
        niceOutputString += self.member_list + '\n'
        niceOutputString += self.advisor + '\n'
        niceOutputString += self.future_work + '\n'
        niceOutputString += self.topic + '\n'
        niceOutputString += self.title + '\n'    
    
    #Basic information about a project.
    board_image_url = models.TextField()
    abstract = models.TextField()
    member_list = models.TextField()
    advisor = models.TextField()
    future_work = models.TextField()
    topic = models.TextField()
    title = models.TextField()
    year = models.TextField()

    #Engineering Class Reference. The CASCADE ensures that if a year is removed, then so are all of the projects for that year.
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE, to_field='degree_program_name')



'''
Project(board_image_url='/myimage.jpg', abstract='This is the abstract', 
member_list='FName, SName, TName', advisor='Dr man', future_work='Awesome future projects',
topic='mtopic', title='mtitle', year='2016')
'''

testProject1 = Project(board_image_url='/myimage.jpg', abstract='In this paper we investigate the use of the area under the receiver operating characteristic (ROC) curve (AUC) as a performance measure for machine learning algorithms. As a case study we evaluate six machine learning algorithms (C4.5, Multiscale Classifier, Perceptron, Multi-layer Perceptron, k-Nearest Neighbours, and a Quadratic Discriminant Function) on six “real world” medical diagnostics data sets. We compare and discuss the use of AUC to the more conventional overall accuracy and find that AUC exhibits a number of desirable properties when compared to overall accuracy: increased sensitivity in Analysis of Variance (ANOVA) tests; a standard error that decreased as both AUC and the number of test samples increased; decision threshold independent; and it is invariant to a priori class probabilities. The paper concludes with the recommendation that AUC be used in preference to overall accuracy for “single number” evaluation of machine learning algorithms.', member_list='FName, SName, TName', advisor='Dr man', future_work='Vinith Misra (Stanford University, USA); Tsachy Weissman (Stanford University, USA) This paper was about universal decoding, sort of. THe idea is that the decoder doesn’t know the codebook but it knows the encoder is using a random block code. However, it doesn’t know the rate, even. The question is really what can one say in this setting? For example, symmetry dictates that the actual message label will be impossible to determine, so the error criterion has to be adjusted accordingly. The decoding strategy that they propose is a partition of the output space (or “clustering”) followed by a labeling. They claim this is a model for clustering through an information theoretic lens, but since the number of clusters is exponential in the dimension of the space, I think that it’s perhaps more of a special case of clustering. A key concept in their development is something they call the minimum partition information, which takes the place of the maximum mutual information (MMI) used in universal decoding (c.f. Csiszr and Krner).',topic='Machine Learning', title='Smart Connected Health 1', year='2016')
testProject2 = Project(board_image_url='/myimage.jpg', abstract='In this paper we investigate the use of the area under the receiver operating characteristic (ROC) curve (AUC) as a performance measure for machine learning algorithms. As a case study we evaluate six machine learning algorithms (C4.5, Multiscale Classifier, Perceptron, Multi-layer Perceptron, k-Nearest Neighbours, and a Quadratic Discriminant Function) on six “real world” medical diagnostics data sets. We compare and discuss the use of AUC to the more conventional overall accuracy and find that AUC exhibits a number of desirable properties when compared to overall accuracy: increased sensitivity in Analysis of Variance (ANOVA) tests; a standard error that decreased as both AUC and the number of test samples increased; decision threshold independent; and it is invariant to a priori class probabilities. The paper concludes with the recommendation that AUC be used in preference to overall accuracy for “single number” evaluation of machine learning algorithms.', member_list='FName, SName, TName', advisor='Dr man', future_work='Vinith Misra (Stanford University, USA); Tsachy Weissman (Stanford University, USA) This paper was about universal decoding, sort of. THe idea is that the decoder doesn’t know the codebook but it knows the encoder is using a random block code. However, it doesn’t know the rate, even. The question is really what can one say in this setting? For example, symmetry dictates that the actual message label will be impossible to determine, so the error criterion has to be adjusted accordingly. The decoding strategy that they propose is a partition of the output space (or “clustering”) followed by a labeling. They claim this is a model for clustering through an information theoretic lens, but since the number of clusters is exponential in the dimension of the space, I think that it’s perhaps more of a special case of clustering. A key concept in their development is something they call the minimum partition information, which takes the place of the maximum mutual information (MMI) used in universal decoding (c.f. Csiszr and Krner).',topic='Machine Learning', title='Smart Connected Health 2', year='2016')
testProject3 = Project(board_image_url='/myimage.jpg', abstract='This is the abstract', member_list='First Person, Second Person, Third Person, Fourth Person', advisor='Dr man', future_work='Awesome future projects',topic='mtopic', title='mtitle', year='2015')



degreeProgram1 = DegreeProgram(degree_program_name='electrical_engineering_and_computing_systems')
degreeProgram2 = DegreeProgram(degree_program_name='aerospace_engineering_and_engineering_mechanics')
degreeProgram3 = DegreeProgram(degree_program_name='civil_and_architectural_engineering_and_construction')
degreeProgram4 = DegreeProgram(degree_program_name='biomedical_chemical_and_environmental_engineering')
degreeProgram5 = DegreeProgram(degree_program_name='engineering_education')
degreeProgram6 = DegreeProgram(degree_program_name='mechanical_and_materials_engineering')






















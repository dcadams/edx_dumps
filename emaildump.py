from datetime import datetime


class EmailDump():
    csm_filename = './dump_files/csm.txt'
    users_filename = './dump_files/users.txt'
    completed_filename = './dump_files/completed.txt'
    mooc_users_filename = './results/mooc_users.txt'
    scpd_users_filename = './results/scpd_users.txt'
    scpd_and_mooc_users_filename = './results/scpd_and_mooc_users.txt'
    completed_users_filename = './results/completed.txt'

    csm_dict = {}
    all_users_dict = {}
    scpd_users_dict = {}
    mooc_users_dict = {}
    scpd_and_mooc_users_dict = {}
    completed_dict = {}
    
    scpd_courses = [
                   'course-v1:Education+mathmindsets+selfpaced',
                   'Education/HTLMath/SelfPaced',
                   'Education/XEDUC115N/Summer2014',
                   'course-v1:Education+XEDUC115N-C1+SelfPaced',
                   'course-v1:Engineering+IE301+ongoing',
                   'course-v1:Law+XLAW7058+Resource',
                   'course-v1:Engineering+VDC+ongoing',
                   'course-v1:Education+XEDUC201+SelfPaced',
                   'course-v1:Education+PrepareCCC+Summer2016',
                   ]
    
    ohs_courses = ['course-v1:ohsx+XM452_Fall+Number_Theory',
                   'course-v1:ohsx+XM452_Fall2016+Number_Theory',
                   'course-v1:ohsx+XM452_Spring+Number_Theory',
                   'course-v1:ohsx+XM452_Summer+Number_Theory',
                   'course-v1:ohsx+XM452_Summer2016+Number_Theory',
                   'course-v1:ohsx+XM511_Fall+Linear_Algebra',
                   'course-v1:ohsx+XM511_Fall2016+Linear_Algebra',
                   'course-v1:ohsx+XM511_Spring+Linear_Algebra',
                   'course-v1:ohsx+XM511_Summer+Linear_Algebra',
                   'course-v1:ohsx+XM511_Summer2016+Linear_Algebra',
                   'course-v1:ohsx+XM521_Fall+Multivariable_Differential_Calculus',
                   'course-v1:ohsx+XM521_Fall2016+Multivariable_Differential_Calculus',
                   'course-v1:ohsx+XM521_Spring+Multivariable_Differential_Calculus',
                   'course-v1:ohsx+XM521_Summer+Multivariable_Differential_Calculus',
                   'course-v1:ohsx+XM521_Summer2016+Multivariable_Differential_Calculus',
                   'course-v1:ohsx+XM522_Fall+Multivariable_Integral_Calculus',
                   'course-v1:ohsx+XM522_Fall2016+Multivariable_Integral_Calculus',
                   'course-v1:ohsx+XM522_Spring+Multivariable_Integral_Calculus',
                   'course-v1:ohsx+XM522_Summer+Multivariable_Integral_Calculus',
                   'course-v1:ohsx+XM522_Summer2016+Multivariable_Integral_Calculus',
                   'course-v1:ohsx+XM531_Fall+Differential_Equations',
                   'course-v1:ohsx+XM531_Fall2016+Differential_Equations',
                   'course-v1:ohsx+XM531_Spring+Differential_Equations',
                   'course-v1:ohsx+XM531_Summer+Differential_Equations',
                   'course-v1:ohsx+XM531_Summer2016+Differential_Equations',
                   'course-v1:ohsx+XM606_Fall+Complex_Analysis',
                   'course-v1:ohsx+XM606_Fall2016+Complex_Analysis',
                   'course-v1:ohsx+XM606_Spring+Complex_Analysis',
                   'course-v1:ohsx+XM606_Summer+Complex_Analysis',
                   'course-v1:ohsx+XM606_Summer2016+Complex_Analysis',
                   'course-v1:ohsx+XM609_Fall+Modern_Algebra',
                   'course-v1:ohsx+XM609_Fall2016+Modern_Algebra',
                   'course-v1:ohsx+XM609_Spring+Modern_Algebra',
                   'course-v1:ohsx+XM609_Summer+Modern_Algebra',
                   'course-v1:ohsx+XM609_Summer2016+Modern_Algebra',
                   'course-v1:ohsx+XM615_Fall+Real_Analysis',
                   'course-v1:ohsx+XM615_Fall2016+Real_Analysis',
                   'course-v1:ohsx+XM615_Spring+Real_Analysis',
                   'course-v1:ohsx+XM615_Summer+Real_Analysis',
                   'course-v1:ohsx+XM615_Summer2016+Real_Analysis',
                   'course-v1:ohsx+XM631_Fall+Partial_Differential_Equations',
                   'course-v1:ohsx+XM631_Fall2016+Partial_Differential_Equations',
                   'course-v1:ohsx+XM631_Spring+Partial_Differential_Equations',
                   'course-v1:ohsx+XM631_Summer+Partial_Differential_Equations',
                   'course-v1:ohsx+XM631_Summer2016+Partial_Differential_Equations',
                   'course-v1:ohsx+XP645_Fall+Light_and_Heat',
                   'course-v1:ohsx+XP645_Light_and_Heat+Summer2016',
                   'course-v1:ohsx+XP645_Spring+Light_and_Heat',
                   'course-v1:ohsx+XP645_Summer+Light_and_Heat',
                   'course-v1:ohsx+XP670_Fall+Modern_Physics',
                   'course-v1:ohsx+XP670_Modern_Physics+Summer2016',
                   'course-v1:ohsx+XP670_Spring+Modern_Physics',
                   'course-v1:ohsx+XP670_Summer+Modern_Physics',
                   'course-v1:ohsx+XP710_Fall+Intermediate_Mechanics_I',
                   'course-v1:ohsx+XP710_Fall2016+Intermediate_Mechanics_I',
                   'course-v1:ohsx+XP710_Intermediate_Mechanics_I+Summer2016',
                   'course-v1:ohsx+XP710_Spring+Intermediate_Mechanics_I',
                   'course-v1:ohsx+XP710_Summer+Intermediate_Mechanics_I',
                   'course-v1:ohsx+XP711_Fall+Intermediate_Mechanics_II',
                   'course-v1:ohsx+XP711_Intermediate_Mechanics_II+Summer2016',
                   'course-v1:ohsx+XP711_Spring+Intermediate_Mechanics_II',
                   'course-v1:ohsx+XP711_Summer+Intermediate_Mechanics_II',
                   'course-v1:ohsx+XP730_Fall+Introduction_to_Quantum_Mechanics',
                   'course-v1:ohsx+XP730_Spring+Introduction_to_Quantum_Mechanics',
                   'course-v1:ohsx+XP730_Summer+Introduction_to_Quantum_Mechanics',
                   'ohs/OB011_Winter2013/Advanced_topics_in_Biological_Research',
                   'ohs/OCRA1_Winter2013/Critical_Reading_and_Argumentation',
                   'ohs/UM157_Winter2013/Logic_in_Action',
                   'ohsx/001/shared_static_assets',
                   'ohsx/SCA25H_Summer2014/Quantum_Foundations_and_Quantum_Information',
                   'ohsx/SCA25H_Summer2015/Quantum_Foundations_and_Quantum_Information',
                   'ohsx/X045_1_Winter2013/Genocide_and_Humanitarian_Intervention',
                   'ohsx/X046_3_Winter2013/Monsters',
                   'ohsx/XM452_Fall2015/Number_Theory',
                   'ohsx/XM452_Spring2015/Number_Theory',
                   'ohsx/XM452_Spring2016/Number_Theory',
                   'ohsx/XM452_Summer2015/Number_Theory',
                   'ohsx/XM457_Fall2013_1/Introduction_to_Logic',
                   'ohsx/XM511_Fall2013_1/Linear_Algebra',
                   'ohsx/XM511_Fall2015/Linear_Algebra',
                   'ohsx/XM511_Spring2015/Linear_Algebra',
                   'ohsx/XM511_Spring2016/Linear_Algebra',
                   'ohsx/XM511_Summer2015/Linear_Algebra',
                   'ohsx/XM521_Fall2013_1/Multivariable_Differential_Calculus',
                   'ohsx/XM521_Fall2015/Multivariable_Differential_Calculus',
                   'ohsx/XM521_Spring2015/Multivariable_Differential_Calculus',
                   'ohsx/XM521_Spring2016/Multivariable_Differential_Calculus',
                   'ohsx/XM521_Summer2015/Multivariable_Differential_Calculus',
                   'ohsx/XM522_Fall2013_1/Multivariable_Integral_Calculus',
                   'ohsx/XM522_Fall2015/Multivariable_Integral_Calculus',
                   'ohsx/XM522_Spring2015/Multivariable_Integral_Calculus',
                   'ohsx/XM522_Spring2016/Multivariable_Integral_Calculus',
                   'ohsx/XM522_Summer2015/Multivariable_Integral_Calculus',
                   'ohsx/XM531_Fall2013_1/Differential_Equations',
                   'ohsx/XM531_Fall2015/Differential_Equations',
                   'ohsx/XM531_Spring2015/Differential_Equations',
                   'ohsx/XM531_Spring2016/Differential_Equations',
                   'ohsx/XM531_Summer2015/Differential_Equations',
                   'ohsx/XM606_Fall2015/Complex_Analysis',
                   'ohsx/XM606_Spring2015/Complex_Analysis',
                   'ohsx/XM606_Spring2016/Complex_Analysis',
                   'ohsx/XM606_Summer2015/Complex_Analysis',
                   'ohsx/XM609_Fall2015/Modern_Algebra',
                   'ohsx/XM609_Spring2015/Modern_Algebra',
                   'ohsx/XM609_Spring2016/Modern_Algebra',
                   'ohsx/XM609_Summer2015/Modern_Algebra',
                   'ohsx/XM615_Fall2015/Real_Analysis',
                   'ohsx/XM615_Spring2015/Real_Analysis',
                   'ohsx/XM615_Spring2016/Real_Analysis',
                   'ohsx/XM615_Summer2015/Real_Analysis',
                   'ohsx/XM631_Fall2013_1/Partial_Differential_Equations',
                   'ohsx/XM631_Spring2016/Partial_Differential_Equations',
                   'ohsx/XP645_Fall2015/Light_and_Heat',
                   'ohsx/XP645_Fall2016/Light_and_Heat',
                   'ohsx/XP645_Spring2016/Light_and_Heat',
                   'ohsx/XP645_Summer2016/Light_and_Heat',
                   'ohsx/XP670_Fall2015/Modern_Physics',
                   'ohsx/XP670_Fall2016/Modern_Physics',
                   'ohsx/XP670_Spring2016/Modern_Physics',
                   'ohsx/XP670_Summer2015/Modern_Physics',
                   'ohsx/XP670_Summer2016/Modern_Physics',
                   'ohsx/XP710_Fall2015/Intermediate_Mechanics_I',
                   'ohsx/XP710_Spring2016/Intermediate_Mechanics_I',
                   'ohsx/XP711_Fall2015/Intermediate_Mechanics_II',
                   'ohsx/XP711_Spring2016/Intermediate_Mechanics_II',
                   'ohsx/XP730_Fall2015/Introduction_to_Quantum_Mechanics',
                   ]
    
    oli_courses = ['course-v1:OLI_Carleton+StatReasoning+Raleigh_SOAN239_Spring2017',
                   'course-v1:OLI_COC+Concepts+Master',
                   'course-v1:OLI_CSUMB+ProbStat+Canner_STAT100_4_Fall2016',
                   'course-v1:OLI_CSUMB+ProbStat+Master',
                   'course-v1:OLI_CSUMB+ProbStat+Unfried_STAT100_1_Fall2016',
                   'course-v1:OLI_CSUMB+StatReasoning+Huerth_STAT100_001_Spring2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Huerth_STAT100_001_Spring2018',
                   'course-v1:OLI_CSUMB+StatReasoning+Huerth_STAT100_002_Spring2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Kim_STAT100_004_Spring2018',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_001_Fall2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_002_Fall2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_002_Spring2018',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_003_Spring2018',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_004_Spring2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_005_Spring2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_005_Spring2018',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_006_Spring2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Lippi_STAT100_0203_Fall2016',
                   'course-v1:OLI_CSUMB+StatReasoning+Potter_STAT100_003_Fall2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Swift_STAT100_004_Fall2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Swift_STAT100_005_Fall2017',
                   'course-v1:OLI_CSUMB+StatReasoning+Williams_STAT100_41541_Fall2016',
                   'course-v1:OLI_CSUMB+StatReasoning+Wisneski_STAT100_001_Summer2017',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_054_Spring2018',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_066_Spring2018',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_075_Spring2018',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_120_Spring2017',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_123_Fall2016',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_129_Spring2017',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_135_Fall2016',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_165_Fall2017',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Box_Math1070_174_Fall2017',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Hendricks_Math1070_144_Spring2017',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Hendricks_Math1070_150_Spring2017',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Hendricks_Math1070_159_Fall2016',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Hendricks_Math1070_165_Fall2016',
                   'course-v1:OLI_GSU-Perimeter+ProbStat+Master',
                   'course-v1:OLI_GSU+ProbStat+Master',
                   'course-v1:OLI_GSU+ProbStat+Math1070_Fall2017',
                   'course-v1:OLI_GSU+ProbStat+Math1070_Maymester2018',
                   'course-v1:OLI_GSU+ProbStat+Math1070_Spring2017',
                   'course-v1:OLI_GSU+ProbStat+Math1070_Spring2018',
                   'course-v1:OLI_GSU+ProbStat+Math1070_Summer2017',
                   'course-v1:OLI_GSU+ProbStat+Math1070_Summer2018',
                   'course-v1:OLI_KTH+PrinciplesOfComputing+Master',
                   'course-v1:OLI_UBC+StatReasoning+Roll_LAIS609C_001_20162017W2',
                   'course-v1:OLI_UCLA+StatReasoning+Stigler_PSYC100A_001_Winter2017',
                   'course-v1:OLI_WGU+ProbStat+Master',
                   'course-v1:OLI_WLU+StatReasoning+Garvis_INTR202_01_02_Winter2018',
                   'course-v1:OLI_WLU+StatReasoning+Garvis_INTR202_03_04_05_Fall2017',
                   'course-v1:OLI_WLU+StatReasoning+Garvis_INTR202_3_4_5_Fall2016',
                   'course-v1:OLI+Concepts+Master',
                   'course-v1:OLI+CourseDesign+Open',
                   'course-v1:OLI+ProbStat+2019r',
                   'course-v1:OLI+ProbStat+Master',
                   'course-v1:OLI+ProbStat+Open_Jan2017',
                   'course-v1:OLI+StatReasoning+Master',
                   'course-v1:OLI+TESTTEST+Partner_Sandbox',
                   'OLI/CS101/Summer2015',
                   'OLI/PrinciplesOfComputing/Open',
                   'OLI/ProbStat/Open',
                   'OLI/StatReasoning/Open',
                   'OLI/StatSandbox/Fall2015',
                   ]
    
    def parse_csm_file(self):
        print(datetime.now())
        with open(self.csm_filename, 'r') as fp:
            for i in range(4):
                next(fp)
                
            last_student_id = None
            courses = []
            dates = []
            for line in fp:
                csm_line = [e.strip() for e in line.split('|')]
                course_id = csm_line[2]
                if course_id in self.ohs_courses or course_id in self.oli_courses:
                    continue
                student_id = csm_line[1]
                date = csm_line[3][:10]
                
                # First student
                if not last_student_id and (student_id != last_student_id):
                    courses.append(course_id)
                    dates.append(date)
                    
                # Same student
                elif student_id == last_student_id:
                    courses.append(course_id)
                    dates.append(date)
                    
                # Different student
                else:
                    self.csm_dict[last_student_id] = [courses, dates]
                    courses = [course_id]
                    dates = [date]
                    
                last_student_id = student_id
        
        # Add last line
        if student_id in self.csm_dict:
            self.csm_dict[student_id][0].append(course_id)
            self.csm_dict[student_id][1].append(date)
        else:
            self.csm_dict[student_id] = [[course_id], [date]]

        print('Processed csm file')
        print(len(self.csm_dict))
        
    def parse_users_file(self):
        print(datetime.now())
        with open(self.users_filename, 'r') as fp:
            for i in range(4):
                next(fp)
            
            for line in fp:
                users_line = [e.strip() for e in line.split('|')]
                student_id = users_line[1]
                username = users_line[2]
                name = users_line[3]
                email = users_line[4]
                date = users_line[5][:10]

                self.all_users_dict[student_id] = [username, name, email, date]

        print('Processed users file')
        print(len(self.all_users_dict))
        
    def parse_completed_file(self):
        print(datetime.now())
        with open(self.completed_filename, 'r') as fp:
            for i in range(8):
                next(fp)
                
            for line in fp:
                completed_line = [e.strip() for e in line.split('|')]
                student_id = completed_line[1]
                course_id = completed_line[2]
                cert_date = completed_line[3]
                email = completed_line[4]
                name = completed_line[5]
                
                if student_id in self.completed_dict:
                    self.completed_dict[student_id][0].append(course_id)
                    self.completed_dict[student_id][1].append(cert_date)
                else:
                    self.completed_dict[student_id] = [[course_id], [cert_date], email, name]

        print('Processed completed file')
        print(len(self.completed_dict))

    def filter_scpd_users(self):
        for student_id, val in self.csm_dict.items():
            courses = val[0]
            for course in courses:
                if course in self.scpd_courses:
                    self.scpd_users_dict[student_id] = val
                    break

        print('Generated scpd users')
        print(len(self.scpd_users_dict))
        
    def filter_mooc_users(self):
        for student_id, val in self.csm_dict.items():
            if student_id in self.scpd_users_dict:
                continue
            else:
                self.mooc_users_dict[student_id] = val
                
        print('Generated mooc users')
        print(len(self.mooc_users_dict))
    
    def generate_scpd_and_mooc_users(self):
        self.scpd_and_mooc_users_dict = {**self.scpd_users_dict, **self.mooc_users_dict}
        
        print('Generated scpd and mooc users')
        print(len(self.scpd_and_mooc_users_dict))
        
    def dump_users(self):
        dicts_to_dump = [self.mooc_users_dict, self.scpd_users_dict, self.scpd_and_mooc_users_dict]
        files_to_write = [self.mooc_users_filename, self.scpd_users_filename, self.scpd_and_mooc_users_filename]
        user_type = ['mooc users', 'scpd users', 'scpd and mooc users']
        for i in range(len(dicts_to_dump)):
            with open(files_to_write[i], 'w+') as fp:
                print('Writing {user_type} file'.format(user_type=user_type[i]))
                self.write_header(fp)
                for student_id, val in dicts_to_dump[i].items():
                    # Anonymous user
                    if student_id not in self.all_users_dict:
                        continue
                    else:
                        self.write_rows(student_id, val, user_type[i], fp) 


    def write_header(self, fp):
        header = "student_id\temail\tusername\tname\tdate registered\tcourse_id\tlast_activity_date\n"
        fp.write(header)

    def write_rows(self, student_id, val, user_type, fp):

        def write_row(student_id, student_details, course, date, fp): 
            row = student_id + "\t"
            row += student_details[2] + "\t"
            row += student_details[0] + "\t"
            row += student_details[1] + "\t"
            row += student_details[3] + "\t"
            row += course + "\t" + date + "\n"
            fp.write(row) 

        student_details = self.all_users_dict[student_id]
        for i in range(len(val[0])):
            # Only write out mooc courses
            if user_type == 'mooc users' and val[0][i] not in self.scpd_courses:
                write_row(student_id, student_details, val[0][i], val[1][i], fp)
            # Only write out scpd courses
            elif user_type == 'scpd users' and val[0][i] in self.scpd_courses:
                write_row(student_id, student_details, val[0][i], val[1][i], fp)
            # Write out all courses
            elif user_type == 'scpd and mooc users':
                write_row(student_id, student_details, val[0][i], val[1][i], fp)
        
    def dump_completed(self):
        with open(self.completed_users_filename, 'w+') as fp:
            print('Writing completed user file')
            self.write_completed_header(fp)
            for student_id, val in self.completed_dict.items():
                courses = val[0]
                for i, course in enumerate(courses):
                    row = student_id + "\t"
                    row += course + "\t"
                    row += val[1][i] + "\t"
                    row += val[2] + "\t"
                    row += val[3] + "\n"
                    fp.write(row)
            
    def write_completed_header(self, fp):
        header = "student_id\tcourse_id\tcert_date\temail\tname\n"
        fp.write(header)            
    

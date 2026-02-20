def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages

def classify_grades(averages):
   (Local scope)
    grade_a = 90
    grade_b = 75
    grade_c = 60
    
    results = {}
    for name, avg in averages.items():
        if avg >= grade_a:
            grade = 'A'
        elif avg >= grade_b:
            grade = 'B'
        elif avg >= grade_c:
            grade = 'C'
        else:
            grade = 'F'
        results[name] = (avg, grade)
    return results

def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    passed_count = 0
    total_students = len(classified)
    
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
        
    
        print(f"{name:<10} | Avg: {avg:<5.2f} | Grade: {grade} | Status: {status}")
    
    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total_students - passed_count}")
    
    return passed_count

# Main Block
if __name__ == "__main__":
    # Sample Data
    student_data = {
        "Alice": [80, 85, 90, 90],
        "Bob": [60, 65, 60, 65],
        "Clara": [95, 98, 92, 100]
    }
    
 
    avg_scores = process_scores(student_data)
    graded_data = classify_grades(avg_scores)
    total_passed = generate_report(graded_data)
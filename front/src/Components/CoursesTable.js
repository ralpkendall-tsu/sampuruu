import React, { useState, useEffect } from 'react';

const CoursesTable = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        fetch("courses")
            .then(response => response.json())
            .then(data => setCourses(data))
    }, []);

    return (
        <div className='container'>
            {courses.map(course => (
                <div key={course.id}>
                    <h1>{course.title}</h1>
                    <p>{course.description}</p>
                    <p>Instructor: {course.instructor}</p>
                    <img src={course.instructorIcon}  width='300px' alt={course.instructor} />
                    <hr />
                    <br />
                </div>
            ))}
        </div>
    );
};

export default CoursesTable;

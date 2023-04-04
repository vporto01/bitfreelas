document.addEventListener('DOMContentLoaded', function () {
    const projectTypeSelect = document.querySelector('#id_project_type');
    const hourlyRateField = document.querySelector('#id_hourly_rate').parentElement.parentElement;
    if (projectTypeSelect.value === 'fixed') {
        hourlyRateField.style.display = 'none';
    }

    projectTypeSelect.addEventListener('change', function () {
        if (projectTypeSelect.value === 'hourly') {
            hourlyRateField.style.display = '';
        } else {
            hourlyRateField.style.display = 'none';
        }
    });
});

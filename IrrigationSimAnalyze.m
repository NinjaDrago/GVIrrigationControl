% Load CSV file
% Replace 'data.csv' with your actual file name
data = csvread('data.csv', 1, 0);  
% (1 skips the header row, 0 means start from first column)

% Extract columns
time       = data(:,1);  % Time(s)
height     = data(:,2);  % Reservoir height (m)
flow_rate  = data(:,3);  % Flow rate (L/s)
velocity   = data(:,4);  % Velocity (m/s)
purge_time = data(:,5);  % Purge time (s)
cumulated  = data(:,6);  % Cumulated delivered (L)

% ---- Plot 1: Accumulated liters per time ----
figure;
plot(time, cumulated, 'b-', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Cumulated Delivered (L)');
title('Accumulated Liters vs Time');
grid on;

% ---- Plot 2: Reservoir height loss vs time ----
height_loss = height(1) - height;
figure;
plot(time, height_loss, 'r-', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Height Loss (m)');
title('Reservoir Height Loss vs Time');
grid on;

% ---- Plot 3: Flow rate vs time ----
figure;
plot(time, flow_rate, 'g-', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Flow Rate (L/s)');
title('Flow Rate vs Time');
grid on;

% ---- Plot 4: Velocity vs time ----
figure;
plot(time, velocity, 'm-', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Velocity (m/s)');
title('Velocity vs Time');
grid on;

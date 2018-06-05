function [H, theta, rho] = hough_lines_acc(BW, varargin)
    % Compute Hough accumulator array for finding lines.
    %
    % BW: Binary (black and white) image containing edge pixels
    % RhoResolution (optional): Difference between successive rho values, in pixels
    % Theta (optional): Vector of theta values to use, in degrees
    %
    % Please see the Matlab documentation for hough():
    % http://www.mathworks.com/help/images/ref/hough.html
    % Your code should imitate the Matlab implementation.
    %
    % Pay close attention to the coordinate system specified in the assignment.
    % Note: Rows of H should correspond to values of rho, columns those of theta.

    %% Parse input arguments
    p = inputParser();
    addParameter(p, 'RhoResolution', 1);
    addParameter(p, 'Theta', linspace(-90, 89, 180));
    parse(p, varargin{:});

    rhoStep = p.Results.RhoResolution;
    theta = p.Results.Theta;

    %% TODO: Your code here
    
    H = zeros(180,size(edgeImg,1));
    
    % Find non-zero pixels i.e. edge points
    [edgePointsX,edgePointsY] = find(BW);
    
    for ii  = 1 : size(edgePointsX)
      
      for theta = 0 : 180
        
        rho  = edgePointsX(ii) * cos(theta) + edgePointsY * sin(theta);
        
        H(theta,rho) =+ 1; 
        
      end
      
      
      
    end
end

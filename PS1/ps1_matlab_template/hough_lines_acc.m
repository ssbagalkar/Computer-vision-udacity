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
    
    % Retrieve the size of image
    [imgHeight, imgWidth] = size(BW);
    
    % Get the max distance i.e the diagonal of image
    distMax = round(sqrt(imgHeight * imgHeight + imgWidth * imgWidth ) );
    
    theta = [-90 : 1 : 89];
    rho = [-distMax : 1 : distMax] ;
    
    %generate the accumulator array
    H = zeros(length(rho),length(theta));
    
    % Scan through the edge image
    for x = 1 : imgWidth
      for y = 1 : imgHeight
        if BW(y,x) ~= 0     % if this is an edge point
          
          for iTheta = 1 : length(theta)
            thetaRadians = theta(iTheta)*pi/180;  % get angle in radians 
            
            %Calculate distance from origin given this angle in radians
            dist = x*cos(thetaRadians) + y*sin(thetaRadians);
            
            % Find the rho index closest to the dist 
            [d, iRho] = min(abs(rho-dist));
          
            if d <= 1
              H(iRho,iTheta) = H(iRho,iTheta) + 1;
            end
          
          end
        end
      end
    end
    
    % Convert to uint8
    H = uint8(255 * mat2gray(H));
end

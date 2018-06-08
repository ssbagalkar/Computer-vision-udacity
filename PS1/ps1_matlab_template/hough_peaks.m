function peaks = hough_peaks(H, numpeaks, varargin)
    % Find peaks in a Hough accumulator array.
    %
    % Threshold (optional): Threshold at which values of H are considered to be peaks
    % NHoodSize (optional): Size of the suppression neighborhood, [M N]
    %
    % Please see the Matlab documentation for houghpeaks():
    % http://www.mathworks.com/help/images/ref/houghpeaks.html
    % Your code should imitate the matlab implementation.

    % TODO: Your code here
    if nargin == 3
       nhood = size(H)/50;
       % Make sure the neighborhood size is odd.
       nhood = max(2*ceil(nhood/2) + 1, 1);
       threshold = varargin{1};
    end
    
    if nargin == 2 
       nhood = size(H)/50;
       % Make sure the neighborhood size is odd.
       nhood = max(2*ceil(nhood/2) + 1, 1);
       threshold = 0.5 * max(H(:));
    end

    done = false;
    hnew = H; r = []; c = [];
    while ~done
       [p, q] = find(hnew == max(hnew(:)));
       p = p(1); q = q(1);
       if hnew(p, q) >= threshold
          r(end + 1) = p; c(end + 1) = q;

          % Suppress this maximum and its close neighbors.
          p1 = p - (nhood(1) - 1)/2; p2 = p + (nhood(1) - 1)/2;
          q1 = q - (nhood(2) - 1)/2; q2 = q + (nhood(2) - 1)/2;
          [pp, qq] = ndgrid(p1:p2,q1:q2);
          pp = pp(:); qq = qq(:);

          % Throw away neighbor coordinates that are out of bounds in
          % the rho direction.
          badrho = find((pp < 1) | (pp > size(H, 1)));
          pp(badrho) = []; qq(badrho) = [];

          % For coordinates that are out of bounds in the theta
          % direction, we want to consider that H is antisymmetric
          % along the rho axis for theta = +/- 90 degrees.
          theta_too_low = find(qq < 1);
          qq(theta_too_low) = size(H, 2) + qq(theta_too_low);
          pp(theta_too_low) = size(H, 1) - pp(theta_too_low) + 1;
          theta_too_high = find(qq > size(H, 2));
          qq(theta_too_high) = qq(theta_too_high) - size(H, 2);
          pp(theta_too_high) = size(H, 1) - pp(theta_too_high) + 1;

          % Convert to linear indices to zero out all the values.
          hnew(sub2ind(size(hnew), pp, qq)) = 0;

          done = length(r) == numpeaks;
       else
          done = true;
       end
    end
    peaks = [r' c'];
end

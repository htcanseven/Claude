function hsbook_style(fig, height_cm, stem)
%HSBOOK_STYLE  Put a MATLAB figure into the house style of the high-speed book.
%
%   hsbook_style(fig, height_cm) restyles figure FIG in place:
%     - full text width, 15.92 cm, and the given height;
%     - every text object in Times New Roman at 11 pt, regular weight
%       (the body font and size of the manuscript);
%     - axes frame and ticks 0.6 pt, ticks inward on all four sides, a light
%       grey grid behind the data;
%     - data lines 1.2 pt, the first four lines in each axes in the house
%       colours, each paired with its own line style so the graph still
%       reads in greyscale print;
%     - no axes titles (the caption is the title), no legend box.
%
%   hsbook_style(fig, height_cm, stem) also writes STEM.png (600 dpi) and
%   STEM.pdf (vector) at exactly that size. Insert the PNG into Word at
%   100 % so that 11 pt in the figure prints at 11 pt on the page.
%
%   Example
%       plot(x, y1, x, y2)
%       xlabel('Rotational speed \itn\rm (r/min)')
%       ylabel('Loss \itP\rm_{loss} (kW)')
%       hsbook_style(gcf, 8.5, 'fig_4_07')
%
%   The rules are those of House_Style.md; the Python twin is hsbook_style.py.
%   Written without access to a MATLAB session: check the first exported
%   figure by eye, and report anything it gets wrong so it can be fixed for
%   every contributor at once.

W_CM    = 15.92;                 % text-block width; change only if the publisher's trim changes
FONT    = 'Times New Roman';
SIZE    = 11;                    % pt
LW_DATA = 1.2;                   % pt
LW_AXES = 0.6;                   % pt
COLOURS = [0x1f 0x4e 0x79;       % blue,  solid
           0xa6 0x35 0x0f;       % rust,  dashed
           0x4a 0x7c 0x1f;       % green, dash-dot
           0x1a 0x1a 0x1a] / 255;% ink,   dotted
STYLES  = {'-', '--', '-.', ':'};
GRID    = [0.85 0.85 0.85];

if nargin < 1 || isempty(fig),       fig = gcf;              end
if nargin < 2 || isempty(height_cm), height_cm = 0.55 * W_CM; end

% --- size: exactly the text width, on screen and on paper -----------------
set(fig, 'Units', 'centimeters', 'Color', 'w');
pos = get(fig, 'Position');
set(fig, 'Position', [pos(1) pos(2) W_CM height_cm]);
set(fig, 'PaperUnits', 'centimeters', 'PaperSize', [W_CM height_cm], ...
         'PaperPositionMode', 'manual', 'PaperPosition', [0 0 W_CM height_cm]);

% --- every text object: house font, house size, regular weight --------------
set(findall(fig, '-property', 'FontName'),   'FontName',   FONT);
set(findall(fig, '-property', 'FontSize'),   'FontSize',   SIZE);
set(findall(fig, '-property', 'FontWeight'), 'FontWeight', 'normal');

% --- axes and data -----------------------------------------------------------
axs = findall(fig, 'Type', 'axes');
for a = reshape(axs, 1, [])
    set(a, 'LineWidth', LW_AXES, 'TickDir', 'in', 'Box', 'on', ...
           'XGrid', 'on', 'YGrid', 'on', 'GridColor', GRID, 'GridAlpha', 1, ...
           'XColor', COLOURS(4, :), 'YColor', COLOURS(4, :), ...
           'TickLength', [0.010 0.010], 'Layer', 'top');
    title(a, '');                                    % the caption is the title
    lines = flipud(findobj(a, 'Type', 'line'));      % in plotting order
    for k = 1:numel(lines)
        set(lines(k), 'LineWidth', LW_DATA);
        if k <= size(COLOURS, 1)
            set(lines(k), 'Color', COLOURS(k, :), 'LineStyle', STYLES{k});
        end
    end
end
set(findall(fig, 'Type', 'legend'), 'Box', 'off');

% --- export at exactly that size ---------------------------------------------
% print() honours PaperPosition; exportgraphics() would crop the figure to its
% content and so change the width it was built at, which is the one thing the
% house style forbids.
if nargin >= 3 && ~isempty(stem)
    print(fig, [stem '.png'], '-dpng', '-r600');
    try
        print(fig, [stem '.pdf'], '-dpdf', '-vector');     % R2022a and later
    catch
        print(fig, [stem '.pdf'], '-dpdf', '-painters');   % earlier releases
    end
end
end

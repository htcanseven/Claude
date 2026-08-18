% export_brno_data.m
% One-time export of the Brno CEITEC dataset (Zenodo 10.5281/zenodo.15233529)
% from MATLAB timeseries objects to plain .csv, so all downstream analysis
% (residuals, statistics, paper figures) can run outside MATLAB.
%
% Usage:
%   1) Unzip the Zenodo archive.
%   2) Set dataRoot below to the unzipped folder.
%   3) Run. One CSV per recording appears in ./exported/, with a column per
%      signal channel and a shared time base.
%
% Requires only base MATLAB (no toolboxes).

dataRoot = "Discrete_Time_Modeling_of_Interturn_Short_Circuits_in_Interior_PMSMs-data_and_models";
outDir   = "exported";
if ~exist(outDir, "dir"); mkdir(outDir); end

matFiles = [dir(fullfile(dataRoot, "Data_diverse_FI", "*.mat"));
            dir(fullfile(dataRoot, "Data_diverse_OC", "*.mat"))];

for k = 1:numel(matFiles)
    inPath = fullfile(matFiles(k).folder, matFiles(k).name);
    S = load(inPath);
    names = fieldnames(S);

    T = table();
    for j = 1:numel(names)
        v = S.(names{j});
        if ~isa(v, "timeseries"); continue; end
        if isempty(T)
            T.time = v.Time(:);
        end
        d = squeeze(v.Data);
        if size(d,1) ~= height(T); d = d.'; end          % channels along columns
        nCh = size(d, 2);
        for c = 1:nCh
            col = names{j};
            if nCh > 1; col = sprintf("%s_%d", names{j}, c); end
            % pad/truncate guard: all series in a file share the time base,
            % but fail loudly if one does not
            assert(size(d,1) == height(T), "%s: length mismatch in %s", ...
                   matFiles(k).name, names{j});
            T.(col) = d(:, c);
        end
    end

    [~, base, ~] = fileparts(matFiles(k).name);
    outPath = fullfile(outDir, base + ".csv");
    writetable(T, outPath);
    fprintf("%-32s -> %s  (%d rows, %d cols)\n", ...
            matFiles(k).name, outPath, height(T), width(T));
end

fprintf("\nDone. Zip the ''exported'' folder and add it to the repo/session.\n");

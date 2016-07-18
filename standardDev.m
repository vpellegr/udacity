clear all; close all; clc;
sample =[18,18,20,21,22,23,21,17,15]';
% [38946, 43420,49191,50430,50557, 52580,53595,54135,60181,62076]';
mean_sample = mean(sample);
deviations = sample - mean_sample*ones(length(sample),1);
dev_squared = deviations.^2;
av_sq_dev = sum(dev_squared)/length(sample)
st_dev = sqrt(av_sq_dev)
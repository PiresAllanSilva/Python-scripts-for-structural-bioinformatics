import os
import sys
import argparse

def make_docking(folder, output, receptor, ligand, config, i, exhaustiveness):
	output_folder = receptor+"_"+ligand
	os.system(f"mkdir {output}/{receptor}/{output_folder}/log \
	{output}/{receptor}/{output_folder}/results")
	os.system(f"vina --receptor {folder}/{receptor} --ligand {folder}/{ligand} --config {folder}/{config} \
		--exhaustiveness {exhaustiveness} --out {output}/{output_folder}/results/{receptor_name}_{ligand_name}_{i}.pdbqt \
		--log {output}/{output_folder}/results/{receptor_name}_{ligand_name}-{i}.log")

def repeat_docking(folder, receptor, ligand, config, iteration, output, exhaustiveness):
	for i in range(1, iteration):
		make_docking(folder, output, receptor, ligand, config, i, exhaustiveness)

def get_list(pdbqt_list):
	files_list =[]
	with open(pdbqt_list, "r") as lt:
		for line in lt:
			files_list.append(line.rstrip())
	return files_list

def loop(receptor_list, ligand_list, folder, config, interation, output, exhaustiveness):
	os.system(f"mkdir {output}")
	for r in receptor_list:
		os.system(f"mkdir {output}/{r}")	
		for l in ligand_list:
			output_folder = r+"_"+l
			os.system(f"mkdir {output}/{r}/{output_folder}")
			repeat_docking(folder, r, l, config, interation, output, exhaustiveness) 


parser = argparse.ArgumentParser(description = "Make a loop for docking repetitions")
parser.add_argument("-l", "--ligand", required = True, help = "File with ligand names", type=str)
parser.add_argument("-r", "--receptor", required = True, help = "File with receptor names", type=str)
parser.add_argument("-f", "--folder", required = True, help = "Folder containing receptors and ligand .pdbqt", type=str)
parser.add_argument("-c", "--config", nargs='?', default = "config.txt", help = "Config file containing x,y and z centers and size", type=str)
parser.add_argument("-e", "--exhaustiveness", nargs='?', default = 8, help = "Exhaustiviness of the docking. By default 8 will be used", type=int)
parser.add_argument("-of", "--output_folder_name", nargs='?', default = "output", help = "Output folder name. By default a folder named \"output\" will be generated", type=str)
parser.add_argument("-i", "--iterations", nargs='?', default = 2, help = "Number of repetitions. By default 1 will be used", type=int)

args = parser.parse_args()

receptor = get_list(args.receptor.rstrip())
ligand = get_list(args.ligand)
loop(receptor, ligand, args.folder, args.config, args.iterations, args.output_folder_name, args.exhaustiveness) 
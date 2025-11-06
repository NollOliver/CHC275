"""
Read two 20-day snapshot files (Day1_20.txt and Day21_40.txt), compute 20-day averages
for each ticker, and write a `report.txt` that lists each ticker with both averages and
indicates which tickers improved (day21-40 average > day1-20 average).

The script uses try/except/else for file I/O and validates parsed data.
It accepts input lines in formats like:
  NVDA,100.5,101.2,...
or
  NVDA 100.5 101.2 ...

Save this file as Fileio.py and run it in the same folder as the input files.
"""

import sys
import os


def parse_snapshot_file(path):
	"""Parse a snapshot file into a dict: ticker -> list of float values.

	Expected per-line formats:
	  TICKER, val, val, ...
	  or
	  TICKER val val val ...

	Returns dict. Raises FileNotFoundError if file missing.
	"""
	data = {}
	try:
		f = open(path, 'r')
	except FileNotFoundError:
		# propagate to caller to handle
		raise
	else:
		with f:
			for raw in f:
				line = raw.strip()
				if not line:
					continue
				# choose delimiter
				if ',' in line:
					parts = [p.strip() for p in line.split(',') if p.strip()]
				else:
					parts = line.split()

				if len(parts) < 2:
					# not enough data
					continue

				ticker = parts[0].upper()
				values = []
				for token in parts[1:]:
					# remove common thousand separators or dollar signs
					t = token.replace('$', '').replace(',', '')
					try:
						values.append(float(t))
					except ValueError:
						# skip tokens that are not numbers
						continue

				if values:
					data[ticker] = values

	return data


def average(values):
	return sum(values) / len(values) if values else 0.0


def create_report(day1_path, day2_path, out_path='report.txt'):
	# Read both files with try/except/else
	try:
		day1 = parse_snapshot_file(day1_path)
	except FileNotFoundError:
		print(f"Error: input file not found: {day1_path}")
		return 1

	try:
		day2 = parse_snapshot_file(day2_path)
	except FileNotFoundError:
		print(f"Error: input file not found: {day2_path}")
		return 1

	# Determine tickers to report on: union of keys
	tickers = sorted(set(day1.keys()) | set(day2.keys()))

	# Compute averages and determine buys
	results = {}
	for t in tickers:
		v1 = day1.get(t, [])
		v2 = day2.get(t, [])
		avg1 = average(v1) if v1 else None
		avg2 = average(v2) if v2 else None
		results[t] = (avg1, avg2)

	# Write report using try/except/else
	try:
		fout = open(out_path, 'w')
	except Exception as e:
		print(f"Error: could not open output file {out_path} for writing: {e}")
		return 1
	else:
		with fout:
			fout.write('Ticker, Day1-20_Avg, Day21-40_Avg, Recommendation\n')
			for t in tickers:
				avg1, avg2 = results[t]
				avg1_s = f"{avg1:.4f}" if avg1 is not None else 'N/A'
				avg2_s = f"{avg2:.4f}" if avg2 is not None else 'N/A'
				if avg1 is None or avg2 is None:
					rec = 'INSUFFICIENT DATA'
				else:
					rec = 'BUY' if avg2 > avg1 else 'NO BUY'
				fout.write(f"{t}, {avg1_s}, {avg2_s}, {rec}\n")

	print(f"Report written to {out_path}")
	return 0


if __name__ == '__main__':
	# Default filenames (as described in the task). They can be overridden by args.
	d1 = 'Day1_20.txt'
	d2 = 'Day21_40.txt'
	if len(sys.argv) >= 3:
		d1 = sys.argv[1]
		d2 = sys.argv[2]

	code = create_report(d1, d2)
	# exit with code for CI or caller
	sys.exit(code)


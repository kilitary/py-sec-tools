rule _HQR_data_file_gyohyd
{
	meta:
		description = "HQR data file"
	strings:
		$a = {48000000??020000????0000????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

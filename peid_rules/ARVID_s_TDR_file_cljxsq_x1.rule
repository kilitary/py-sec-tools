rule _ARVID_s_TDR_file_cljxsq
{
	meta:
		description = "ARVID_s TDR file"
	strings:
		$a = {74000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

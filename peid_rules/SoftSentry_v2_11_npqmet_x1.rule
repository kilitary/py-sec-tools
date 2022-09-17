rule _SoftSentry_v2_11_npqmet
{
	meta:
		description = "SoftSentry v2_11"
	strings:
		$a = {558BEC83EC??535657E950}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

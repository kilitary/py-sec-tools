rule _EPW_v1_30_szsaca
{
	meta:
		description = "EPW v1_30"
	strings:
		$a = {06571E5655525153502E8C0608008CC083C0102E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

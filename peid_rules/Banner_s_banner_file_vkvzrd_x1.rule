rule _Banner_s_banner_file_vkvzrd
{
	meta:
		description = "Banner_s banner file"
	strings:
		$a = {D1BA0100}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

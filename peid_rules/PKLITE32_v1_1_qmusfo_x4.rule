rule _PKLITE32_v1_1_qmusfo
{
	meta:
		description = "PKLITE32 v1_1"
	strings:
		$a = {53558BE833DBEB600D0A0D0A57575061636B3332}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

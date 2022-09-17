rule _EmbedPE_v1_24__cyclotron_zfffzm
{
	meta:
		description = "EmbedPE v1_24 __ cyclotron"
	strings:
		$a = {83EC506068????????E8????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

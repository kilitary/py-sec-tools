rule _Ultra_Compressor_s_Archive_yvlvtd
{
	meta:
		description = "Ultra Compressor_s Archive"
	strings:
		$a = {5543321A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

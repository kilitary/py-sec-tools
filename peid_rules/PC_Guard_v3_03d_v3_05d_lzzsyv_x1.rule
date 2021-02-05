rule _PC_Guard_v3_03d_v3_05d_lzzsyv
{
	meta:
		description = "PC_Guard v3_03d_ v3_05d"
	strings:
		$a = {555356515257E816000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

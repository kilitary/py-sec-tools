rule _NX_PE_Packer_v1_0_shxikb
{
	meta:
		description = "NX PE Packer v1_0"
	strings:
		$a = {01AD543A4000FFB5503A40006A40FF95883A4000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

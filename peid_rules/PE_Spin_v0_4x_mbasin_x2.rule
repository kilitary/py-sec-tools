rule _PE_Spin_v0_4x_mbasin
{
	meta:
		description = "PE Spin v0_4x"
	strings:
		$a = {EB016860E8000000008B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

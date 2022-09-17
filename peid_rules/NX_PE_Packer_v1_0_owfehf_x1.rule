rule _NX_PE_Packer_v1_0_owfehf
{
	meta:
		description = "NX PE Packer v1_0"
	strings:
		$a = {FF60FFCAFF00BADC0DE040005000600070008000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

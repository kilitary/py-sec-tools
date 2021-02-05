rule _MEW_10_packer_v1_0__Northfox_xeafca
{
	meta:
		description = "MEW 10 packer v1_0 __ Northfox"
	strings:
		$a = {33C0E9???0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

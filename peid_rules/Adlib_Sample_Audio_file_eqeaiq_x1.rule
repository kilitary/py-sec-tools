rule _Adlib_Sample_Audio_file_eqeaiq
{
	meta:
		description = "Adlib Sample Audio file"
	strings:
		$a = {474F4C442053414D504C45}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

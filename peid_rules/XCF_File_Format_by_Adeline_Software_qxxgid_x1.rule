rule _XCF_File_Format_by_Adeline_Software_qxxgid
{
	meta:
		description = "XCF File Format by Adeline Software"
	strings:
		$a = {4672616D654C656EF40F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

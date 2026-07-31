from fastapi import APIRouter, status

router = APIRouter(tags=["General"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Root endpoint",
)
async def root() -> dict[str, str]:
    """
    Root endpoint to verify the API is running.
    """
    return {
        "message": "Welcome to the Company Brochure API",
        "docs": "/docs",
    }


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health check",
)
async def health_check() -> dict[str, str]:
    """
    Health check endpoint for monitoring and deployment platforms.
    """
    return {
        "status": "healthy",
    }